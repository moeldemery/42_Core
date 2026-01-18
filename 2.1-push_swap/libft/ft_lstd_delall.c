/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstdelall.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: meldemir <meldemir@student.42berlin.d      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/09 15:36:32 by meldemir          #+#    #+#             */
/*   Updated: 2026/01/09 15:36:33 by meldemir         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "libft.h"

void	ft_lstd_delall(t_d_list *lst)
{
	if (lst == NULL )
		return ;
	while (lst)
	{
		free(lst->content);
		lst = lst->next;
	}
	free(lst);
}
